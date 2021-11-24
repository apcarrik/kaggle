def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Distance", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[4]>1:
		# {"feature": "Occupation", "instances": 17, "metric_value": 0.9975, "depth": 2}
		if obj[2]<=11:
			# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[3]>0.0:
				# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[0]>0:
					return 'True'
				elif obj[0]<=0:
					# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]>0:
						return 'False'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[3]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[2]>11:
			# {"feature": "Coupon", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[0]<=2:
				return 'False'
			elif obj[0]>2:
				# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3]<=1.0:
					return 'True'
				elif obj[3]>1.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[4]<=1:
		return 'True'
	else: return 'True'
