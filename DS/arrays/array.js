class MyArray {
    constructor(){
        this.length = 0;
        this.data = {}
    }

    get(index){
        this.data[index];
    }

    push(item){
        this.data[this.length] = item;
        this.length++;
        return this.length;
    }

    pop(){
        const lastItem = this.data[this.length - 1];
        delete this.data[this.length -1];
        this.length--;
        return lastItem
    }
}


const newArray = new MyArray();
newArray.push(12)
newArray.push({'Hi': 'Ho'});
newArray.pop();
console.log(newArray);
