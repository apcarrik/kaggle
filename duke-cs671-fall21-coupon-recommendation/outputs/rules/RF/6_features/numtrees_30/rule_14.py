def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[2]<=2:
		# {"feature": "Occupation", "instances": 24, "metric_value": 0.9183, "depth": 2}
		if obj[3]<=11:
			# {"feature": "Passanger", "instances": 21, "metric_value": 0.7919, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Distance", "instances": 12, "metric_value": 0.9799, "depth": 4}
				if obj[5]<=2:
					# {"feature": "Coupon", "instances": 10, "metric_value": 1.0, "depth": 5}
					if obj[1]>1:
						# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[4]<=1.0:
							return 'False'
						elif obj[4]>1.0:
							return 'True'
						else: return 'True'
					elif obj[1]<=1:
						# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]<=1.0:
							return 'True'
						elif obj[4]>1.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[5]>2:
					return 'True'
				else: return 'True'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		elif obj[3]>11:
			return 'False'
		else: return 'False'
	elif obj[2]>2:
		# {"feature": "Occupation", "instances": 10, "metric_value": 0.7219, "depth": 2}
		if obj[3]>1:
			# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[4]>0.0:
				return 'False'
			elif obj[4]<=0.0:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]>2:
					return 'False'
				elif obj[0]<=2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[3]<=1:
			return 'True'
		else: return 'True'
	else: return 'False'
