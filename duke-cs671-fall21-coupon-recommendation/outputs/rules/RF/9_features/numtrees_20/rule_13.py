def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[2]>0:
		# {"feature": "Education", "instances": 41, "metric_value": 0.965, "depth": 2}
		if obj[3]<=1:
			# {"feature": "Distance", "instances": 21, "metric_value": 0.7025, "depth": 3}
			if obj[8]<=2:
				# {"feature": "Occupation", "instances": 20, "metric_value": 0.6098, "depth": 4}
				if obj[4]>3:
					# {"feature": "Time", "instances": 14, "metric_value": 0.7496, "depth": 5}
					if obj[1]>1:
						# {"feature": "Passanger", "instances": 10, "metric_value": 0.8813, "depth": 6}
						if obj[0]>0:
							# {"feature": "Bar", "instances": 9, "metric_value": 0.7642, "depth": 7}
							if obj[5]<=0.0:
								# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[6]>0.0:
									# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[6]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[5]>0.0:
								return 'True'
							else: return 'True'
						elif obj[0]<=0:
							return 'False'
						else: return 'False'
					elif obj[1]<=1:
						return 'True'
					else: return 'True'
				elif obj[4]<=3:
					return 'True'
				else: return 'True'
			elif obj[8]>2:
				return 'False'
			else: return 'False'
		elif obj[3]>1:
			# {"feature": "Passanger", "instances": 20, "metric_value": 0.971, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Bar", "instances": 11, "metric_value": 0.684, "depth": 4}
				if obj[5]>0.0:
					return 'False'
				elif obj[5]<=0.0:
					# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[1]>0:
						# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]<=16:
							return 'True'
						elif obj[4]>16:
							return 'False'
						else: return 'False'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[0]>1:
				# {"feature": "Distance", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[8]>1:
					# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[1]>0:
						# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[4]<=9:
							# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[5]<=0.0:
								# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[6]>0.0:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								elif obj[6]<=0.0:
									return 'False'
								else: return 'False'
							elif obj[5]>0.0:
								return 'False'
							else: return 'False'
						elif obj[4]>9:
							return 'True'
						else: return 'True'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				elif obj[8]<=1:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]<=0:
		# {"feature": "Passanger", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[0]>0:
			return 'False'
		elif obj[0]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
