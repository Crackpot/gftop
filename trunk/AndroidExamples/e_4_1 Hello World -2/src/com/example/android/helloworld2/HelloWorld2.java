package com.example.android.helloworld2;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.TextView;

/** 建立HelloWorld应用程序 **/
public class HelloWorld2 extends Activity {
	OnClickListener listener1 = null;

	/** Called when the activity is first created. */
	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		/** 当Button01被点击时，监听程序listener1的处理程序 **/
		listener1 = new OnClickListener() {
			@Override
			public void onClick(View v) {
				// TODO Auto-generated method stub
				/** 从显示窗体模板中取得TextView01，定义TextView类，实例化变量text_view **/
				TextView text_view = (TextView) findViewById(R.id.TextView01);
				/** 定义字符序列变量text_view_old，保存旧的信息 **/
				CharSequence text_view_old = text_view.getText();
				/** 加上新的信息，设置TextView01的显示标题 **/
				text_view.setText("修改前：" + text_view_old + "\n"
						+ "增加新的信息：Hello World again!");
			}
		};
		/** 显示main.XML窗体 **/
		setContentView(R.layout.main);
		Button button1 = (Button) findViewById(R.id.Button01);
		button1.setOnClickListener(listener1);
	}
}