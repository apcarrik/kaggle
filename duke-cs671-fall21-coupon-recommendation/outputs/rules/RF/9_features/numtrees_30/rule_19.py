def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Distance", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[8]<=2:
		# {"feature": "Occupation", "instances": 29, "metric_value": 0.8498, "depth": 2}
		if obj[4]<=9:
			# {"feature": "Bar", "instances": 22, "metric_value": 0.684, "depth": 3}
			if obj[5]>0.0:
				# {"feature": "Time", "instances": 14, "metric_value": 0.3712, "depth": 4}
				if obj[1]>0:
					return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			elif obj[5]<=0.0:
				# {"feature": "Time", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Coupon", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[2]>1:
						# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[3]>0:
							return 'True'
						elif obj[3]<=0:
							# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=1.0:
									# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[2]<=1:
						return 'False'
					else: return 'False'
				elif obj[1]>3:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[4]>9:
			# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[1]>1:
				return 'False'
			elif obj[1]<=1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[8]>2:
		return 'False'
	else: return 'False'
