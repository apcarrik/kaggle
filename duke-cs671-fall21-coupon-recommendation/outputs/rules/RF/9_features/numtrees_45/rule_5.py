def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Bar", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[5]<=1.0:
		# {"feature": "Passanger", "instances": 17, "metric_value": 0.9774, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Occupation", "instances": 15, "metric_value": 0.9183, "depth": 3}
			if obj[4]<=14:
				# {"feature": "Coupon", "instances": 12, "metric_value": 0.8113, "depth": 4}
				if obj[2]>1:
					# {"feature": "Time", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[1]>3:
						# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[3]<=0:
							return 'True'
						elif obj[3]>0:
							# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]>1.0:
								return 'True'
							elif obj[6]<=1.0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[1]<=3:
						return 'True'
					else: return 'True'
				elif obj[2]<=1:
					# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[1]<=0:
						# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[6]<=1.0:
							# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[3]<=2:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=1:
									# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]<=1:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[6]>1.0:
							return 'True'
						else: return 'True'
					elif obj[1]>0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[4]>14:
				# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]>0:
					return 'False'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[0]>2:
			return 'False'
		else: return 'False'
	elif obj[5]>1.0:
		return 'True'
	else: return 'True'
