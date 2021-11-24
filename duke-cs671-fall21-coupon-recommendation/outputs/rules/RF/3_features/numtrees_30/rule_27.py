def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[2]<=21:
		# {"feature": "Education", "instances": 32, "metric_value": 0.9284, "depth": 2}
		if obj[1]>1:
			# {"feature": "Coupon", "instances": 17, "metric_value": 0.9975, "depth": 3}
			if obj[0]>0:
				return 'True'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		elif obj[1]<=1:
			# {"feature": "Coupon", "instances": 15, "metric_value": 0.7219, "depth": 3}
			if obj[0]<=3:
				return 'True'
			elif obj[0]>3:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[2]>21:
		return 'False'
	else: return 'False'
