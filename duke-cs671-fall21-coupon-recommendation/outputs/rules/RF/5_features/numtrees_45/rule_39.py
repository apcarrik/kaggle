def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[2]>1:
		# {"feature": "Education", "instances": 21, "metric_value": 0.9852, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Coupon", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[0]<=3:
				# {"feature": "Distance", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[4]>1:
					# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[3]<=1.0:
						return 'True'
					elif obj[3]>1.0:
						return 'True'
					else: return 'True'
				elif obj[4]<=1:
					return 'True'
				else: return 'True'
			elif obj[0]>3:
				return 'False'
			else: return 'False'
		elif obj[1]>2:
			# {"feature": "Coupon", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[0]<=3:
				return 'False'
			elif obj[0]>3:
				# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3]>0.0:
					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]<=2:
						return 'False'
					else: return 'False'
				elif obj[3]<=0.0:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]<=1:
		return 'True'
	else: return 'True'
