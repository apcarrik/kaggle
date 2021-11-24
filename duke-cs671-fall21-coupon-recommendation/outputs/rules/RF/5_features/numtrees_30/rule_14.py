def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[2]>1:
		# {"feature": "Distance", "instances": 32, "metric_value": 0.9972, "depth": 2}
		if obj[4]<=2:
			# {"feature": "Education", "instances": 27, "metric_value": 0.9751, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9986, "depth": 4}
				if obj[3]<=1.0:
					# {"feature": "Coupon", "instances": 13, "metric_value": 0.9612, "depth": 5}
					if obj[0]<=3:
						return 'False'
					elif obj[0]>3:
						return 'False'
					else: return 'False'
				elif obj[3]>1.0:
					# {"feature": "Coupon", "instances": 10, "metric_value": 0.8813, "depth": 5}
					if obj[0]>1:
						return 'True'
					elif obj[0]<=1:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		elif obj[4]>2:
			# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[1]>0:
				return 'False'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]<=1:
		return 'False'
	else: return 'False'
