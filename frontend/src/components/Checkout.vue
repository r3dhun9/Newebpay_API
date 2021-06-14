<template>
  <div class="container">
    <form v-show="firstFormShow">
        <div class="shadow p-3 mb-5 bg-body rounded">
            <label for="productName" class="form-label">商品名稱：</label>
            <input v-model="formData['productName']" readonly class="form-control" id="productName">
        </div>
        <div class="shadow p-3 mb-5 bg-body rounded">
            <label for="productPrice" class="form-label">商品價格：</label>
            <input v-model="formData['productPrice']" readonly class="form-control" id="productPrice">
        </div>
        <div class="shadow p-3 mb-5 bg-body rounded">
            <label for="productQuantity" class="form-label">商品數量：</label>
            <input v-model="formData['productQuantity']" readonly class="form-control" id="productQuantity">
        </div>
        <div class="text-center">
            <button type="submit" class="btn btn-primary" @click.prevent="checkoutProduct">下一步</button>
        </div>
    </form>
    <div v-show="secondFormShow">
        <div class="shadow p-3 mb-5 bg-body rounded">
            <label for="customerName" class="form-label">購買人姓名：</label>
            <input v-model="formData['customerName']" readonly class="form-control" id="customerName">
        </div>
        <div class="shadow p-3 mb-5 bg-body rounded">
            <label for="customerEmail" class="form-label">購買人信箱：</label>
            <input v-model="formData['customerEmail']" readonly class="form-control" id="customerEmail">
        </div>
        <div class="shadow p-3 mb-5 bg-body rounded">
            <label for="customerPhone" class="form-label">購買人電話：</label>
            <input v-model="formData['customerPhone']" readonly class="form-control" id="customerPhone">
        </div>
    </div>
    <form v-show="secondFormShow" action="https://ccore.newebpay.com/MPG/mpg_gateway" method="POST">
        <div style="display:none">
            <input v-model="tradeData['MerchantID']" type="text" name="MerchantID"/>
            <input v-model="tradeData['TradeInfo']" type="text" name="TradeInfo"/>
            <input v-model="tradeData['TradeSha']" type="text" name="TradeSha"/>
            <input v-model="tradeData['Version']" type="text" name="Version"/>
        </div>
        <div class="text-center">
            <button type="submit" class="btn btn-primary">結帳</button>
        </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Checkout',
  data () {
    return {
        firstFormShow: true,
        secondFormShow: false,
        formData: {
            "productName": "【一定好看】77歲富豪娶嫩妻-須藤早貴三個月後離奇暴斃",
            "productPrice": "10000",
            "productQuantity": "1",
            "customerName": "陳靖汯",
            "customerEmail": "redhung@hung.red",
            "customerPhone": "0912345678"
        },
        tradeData: {
            "MerchantID": "MS120725784",
            "TradeInfo": "",
            "TradeSha": "",
            "Version": "1.6"
        },
    }
  },
  methods: {
      checkoutProduct () {
            const backendPath = "http://localhost:8888/checkout"
            axios.post(backendPath, this.formData)
                .then((res) => {
                    this.tradeData['TradeInfo'] = res.data['tradeInfo']
                    this.tradeData['TradeSha'] = res.data['tradeSha']
                    this.firstFormShow = false
                    this.secondFormShow = true
                })
                .catch((error) => {
                    console.error(error)
                })
      },
  }
}
</script>