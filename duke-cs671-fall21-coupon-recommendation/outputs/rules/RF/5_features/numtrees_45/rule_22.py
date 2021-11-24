def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[0]<=3:
		# {"feature": "Education", "instances": 16, "metric_value": 1.0, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.9852, "depth": 3}
			if obj[3]<=2.0:
				# {"feature": "Occupation", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[2]>4:
					# {"feature": "Distance", "instances": 8, "metric_value": 1.0, "depth": 5}
					if obj[4]>1:
						return 'True'
					elif obj[4]<=1:
						return 'False'
					else: return 'False'
				elif obj[2]<=4:
					# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[4]>1:
						return 'True'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[3]>2.0:
				return 'False'
			else: return 'False'
		elif obj[1]>2:
			return 'False'
		else: return 'False'
	elif obj[0]>3:
		# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[1]<=2:
			return 'False'
		elif obj[1]>2:
			return 'True'
		else: return 'True'
	else: return 'False'
