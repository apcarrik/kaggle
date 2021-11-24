def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Occupation", "instances": 85, "metric_value": 0.9774, "depth": 1}
	if obj[2]<=7.752941176470588:
		# {"feature": "Coupon", "instances": 54, "metric_value": 0.9357, "depth": 2}
		if obj[0]>1:
			# {"feature": "Education", "instances": 38, "metric_value": 0.868, "depth": 3}
			if obj[1]<=3:
				return 'True'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		elif obj[0]<=1:
			# {"feature": "Education", "instances": 16, "metric_value": 1.0, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[2]>7.752941176470588:
		# {"feature": "Education", "instances": 31, "metric_value": 0.9992, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Coupon", "instances": 20, "metric_value": 0.971, "depth": 3}
			if obj[0]>1:
				return 'True'
			elif obj[0]<=1:
				return 'False'
			else: return 'False'
		elif obj[1]>2:
			# {"feature": "Coupon", "instances": 11, "metric_value": 0.8454, "depth": 3}
			if obj[0]<=2:
				return 'False'
			elif obj[0]>2:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'False'
