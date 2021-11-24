def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.994, "depth": 2}
		if obj[3]<=2.0:
			# {"feature": "Occupation", "instances": 21, "metric_value": 0.9984, "depth": 3}
			if obj[2]<=9:
				# {"feature": "Distance", "instances": 15, "metric_value": 0.9968, "depth": 4}
				if obj[4]<=2:
					# {"feature": "Coupon", "instances": 13, "metric_value": 0.9612, "depth": 5}
					if obj[0]<=2:
						return 'True'
					elif obj[0]>2:
						return 'True'
					else: return 'True'
				elif obj[4]>2:
					return 'False'
				else: return 'False'
			elif obj[2]>9:
				# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[0]>0:
					# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[4]>1:
						return 'False'
					elif obj[4]<=1:
						return 'False'
					else: return 'False'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[3]>2.0:
			return 'False'
		else: return 'False'
	elif obj[1]>3:
		return 'True'
	else: return 'True'
