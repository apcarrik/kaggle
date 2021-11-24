def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 8147, "metric_value": 0.4722, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 5903, "metric_value": 0.4656, "depth": 2}
		if obj[1]>1:
			# {"feature": "Occupation", "instances": 3341, "metric_value": 0.4743, "depth": 3}
			if obj[2]<=13.280684199513743:
				return 'True'
			elif obj[2]>13.280684199513743:
				return 'True'
			else: return 'True'
		elif obj[1]<=1:
			# {"feature": "Occupation", "instances": 2562, "metric_value": 0.4529, "depth": 3}
			if obj[2]>0:
				return 'True'
			elif obj[2]<=0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Education", "instances": 2244, "metric_value": 0.4844, "depth": 2}
		if obj[1]>0:
			# {"feature": "Occupation", "instances": 1454, "metric_value": 0.4761, "depth": 3}
			if obj[2]<=18.884637515507425:
				return 'False'
			elif obj[2]>18.884637515507425:
				return 'False'
			else: return 'False'
		elif obj[1]<=0:
			# {"feature": "Occupation", "instances": 790, "metric_value": 0.4907, "depth": 3}
			if obj[2]>1.661424080504549:
				return 'True'
			elif obj[2]<=1.661424080504549:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'False'
