def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Distance", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[8]<=2:
		# {"feature": "Occupation", "instances": 45, "metric_value": 0.9996, "depth": 2}
		if obj[4]<=10:
			# {"feature": "Coupon", "instances": 33, "metric_value": 0.9834, "depth": 3}
			if obj[2]>0:
				# {"feature": "Time", "instances": 24, "metric_value": 0.8709, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Education", "instances": 18, "metric_value": 0.9641, "depth": 5}
					if obj[3]<=1:
						# {"feature": "Direction_same", "instances": 10, "metric_value": 0.7219, "depth": 6}
						if obj[7]<=0:
							return 'True'
						elif obj[7]>0:
							# {"feature": "Bar", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[5]>0.0:
								# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[6]>0.0:
									return 'False'
								elif obj[6]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[5]<=0.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[3]>1:
						# {"feature": "Passanger", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[0]>1:
							# {"feature": "Bar", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[5]<=1.0:
								# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[6]>0.0:
									# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								elif obj[6]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[5]>1.0:
								return 'False'
							else: return 'False'
						elif obj[0]<=1:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[1]>3:
					return 'True'
				else: return 'True'
			elif obj[2]<=0:
				# {"feature": "Time", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[1]>0:
					return 'False'
				elif obj[1]<=0:
					# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[5]>1.0:
						return 'True'
					elif obj[5]<=1.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[4]>10:
			# {"feature": "Coupon", "instances": 12, "metric_value": 0.8113, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Bar", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[5]>0.0:
					# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[1]>0:
						return 'False'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				elif obj[5]<=0.0:
					return 'True'
				else: return 'True'
			elif obj[2]>3:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[8]>2:
		return 'False'
	else: return 'False'
