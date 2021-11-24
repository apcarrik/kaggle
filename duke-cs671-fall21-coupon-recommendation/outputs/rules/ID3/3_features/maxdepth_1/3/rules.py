def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 8147, "metric_value": 0.4716, "depth": 1}
	if obj[0]>1:
		# {"feature": "Occupation", "instances": 5887, "metric_value": 0.4654, "depth": 2}
		if obj[2]>0:
			# {"feature": "Education", "instances": 5822, "metric_value": 0.4663, "depth": 3}
			if obj[1]<=4:
				return 'True'
			elif obj[1]>4:
				return 'True'
			else: return 'True'
		elif obj[2]<=0:
			# {"feature": "Education", "instances": 65, "metric_value": 0.3446, "depth": 3}
			if obj[1]<=0:
				return 'True'
			elif obj[1]>0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Occupation", "instances": 2260, "metric_value": 0.4819, "depth": 2}
		if obj[2]>2.0261754612655967:
			# {"feature": "Education", "instances": 1792, "metric_value": 0.4903, "depth": 3}
			if obj[1]>0:
				return 'False'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		elif obj[2]<=2.0261754612655967:
			# {"feature": "Education", "instances": 468, "metric_value": 0.4172, "depth": 3}
			if obj[1]<=3:
				return 'False'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
