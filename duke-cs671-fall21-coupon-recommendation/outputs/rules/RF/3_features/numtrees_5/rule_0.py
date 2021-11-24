def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 204, "metric_value": 0.99, "depth": 1}
	if obj[0]>0:
		# {"feature": "Education", "instances": 171, "metric_value": 0.973, "depth": 2}
		if obj[1]>1:
			# {"feature": "Occupation", "instances": 97, "metric_value": 0.9907, "depth": 3}
			if obj[2]<=20:
				return 'True'
			elif obj[2]>20:
				return 'False'
			else: return 'False'
		elif obj[1]<=1:
			# {"feature": "Occupation", "instances": 74, "metric_value": 0.9353, "depth": 3}
			if obj[2]<=10:
				return 'True'
			elif obj[2]>10:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[0]<=0:
		# {"feature": "Education", "instances": 33, "metric_value": 0.9457, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Occupation", "instances": 29, "metric_value": 0.8936, "depth": 3}
			if obj[2]<=12:
				return 'False'
			elif obj[2]>12:
				return 'True'
			else: return 'True'
		elif obj[1]>3:
			# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[2]>1:
				return 'True'
			elif obj[2]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
