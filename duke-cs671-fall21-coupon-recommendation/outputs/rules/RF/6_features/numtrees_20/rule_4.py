def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Education", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[2]>0:
		# {"feature": "Restaurant20to50", "instances": 35, "metric_value": 0.8631, "depth": 2}
		if obj[4]>0.0:
			# {"feature": "Passanger", "instances": 30, "metric_value": 0.9183, "depth": 3}
			if obj[0]>0:
				# {"feature": "Coupon", "instances": 28, "metric_value": 0.9403, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Distance", "instances": 22, "metric_value": 0.976, "depth": 5}
					if obj[5]<=2:
						# {"feature": "Occupation", "instances": 17, "metric_value": 0.9975, "depth": 6}
						if obj[3]<=11:
							return 'False'
						elif obj[3]>11:
							return 'False'
						else: return 'False'
					elif obj[5]>2:
						# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[3]<=11:
							return 'False'
						elif obj[3]>11:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[1]>3:
					# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[3]<=4:
						# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'False'
						else: return 'False'
					elif obj[3]>4:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		elif obj[4]<=0.0:
			return 'False'
		else: return 'False'
	elif obj[2]<=0:
		# {"feature": "Coupon", "instances": 16, "metric_value": 0.5436, "depth": 2}
		if obj[1]>1:
			return 'True'
		elif obj[1]<=1:
			# {"feature": "Occupation", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[3]>1:
				return 'False'
			elif obj[3]<=1:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
