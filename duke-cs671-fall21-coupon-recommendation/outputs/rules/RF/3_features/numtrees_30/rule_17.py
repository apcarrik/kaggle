def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Education", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Occupation", "instances": 28, "metric_value": 0.9963, "depth": 2}
		if obj[2]>1:
			# {"feature": "Coupon", "instances": 23, "metric_value": 0.9656, "depth": 3}
			if obj[0]>0:
				return 'True'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		elif obj[2]<=1:
			# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[0]>0:
				return 'False'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[1]>2:
		return 'False'
	else: return 'False'
