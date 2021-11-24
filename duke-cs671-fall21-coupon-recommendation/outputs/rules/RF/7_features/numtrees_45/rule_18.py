def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[4]>-1.0:
		# {"feature": "Occupation", "instances": 22, "metric_value": 0.9024, "depth": 2}
		if obj[3]>2:
			# {"feature": "Distance", "instances": 12, "metric_value": 0.65, "depth": 3}
			if obj[6]>1:
				# {"feature": "Coupon", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[1]>1:
					# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[2]>2:
						return 'True'
					else: return 'True'
				elif obj[1]<=1:
					return 'False'
				else: return 'False'
			elif obj[6]<=1:
				return 'True'
			else: return 'True'
		elif obj[3]<=2:
			# {"feature": "Education", "instances": 10, "metric_value": 1.0, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Passanger", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Coupon", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[1]>1:
						# {"feature": "Direction_same", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[5]>0:
							# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=1:
								return 'True'
							else: return 'True'
						elif obj[5]<=0:
							# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=1:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[1]<=1:
						return 'False'
					else: return 'False'
				elif obj[0]>1:
					return 'False'
				else: return 'False'
			elif obj[2]>3:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[4]<=-1.0:
		return 'False'
	else: return 'False'
