def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[3]<=2.0:
		# {"feature": "Distance", "instances": 20, "metric_value": 0.8813, "depth": 2}
		if obj[4]>1:
			# {"feature": "Occupation", "instances": 16, "metric_value": 0.6962, "depth": 3}
			if obj[2]<=7:
				# {"feature": "Education", "instances": 12, "metric_value": 0.8113, "depth": 4}
				if obj[1]>0:
					# {"feature": "Coupon", "instances": 10, "metric_value": 0.8813, "depth": 5}
					if obj[0]>0:
						return 'False'
					elif obj[0]<=0:
						return 'False'
					else: return 'False'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			elif obj[2]>7:
				return 'False'
			else: return 'False'
		elif obj[4]<=1:
			# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[3]>2.0:
		return 'True'
	else: return 'True'
