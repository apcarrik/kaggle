def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Education", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[3]<=3:
		# {"feature": "Coffeehouse", "instances": 45, "metric_value": 0.9911, "depth": 2}
		if obj[6]>1.0:
			# {"feature": "Coupon", "instances": 23, "metric_value": 0.9877, "depth": 3}
			if obj[2]>0:
				# {"feature": "Distance", "instances": 21, "metric_value": 0.9587, "depth": 4}
				if obj[9]>1:
					# {"feature": "Occupation", "instances": 15, "metric_value": 0.8366, "depth": 5}
					if obj[4]<=20:
						# {"feature": "Time", "instances": 14, "metric_value": 0.7496, "depth": 6}
						if obj[1]>0:
							# {"feature": "Passanger", "instances": 10, "metric_value": 0.469, "depth": 7}
							if obj[0]<=1:
								return 'True'
							elif obj[0]>1:
								# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[7]>1.0:
									return 'True'
								elif obj[7]<=1.0:
									# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[5]<=0.0:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[1]<=0:
							# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[7]<=1.0:
								return 'True'
							elif obj[7]>1.0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[4]>20:
						return 'False'
					else: return 'False'
				elif obj[9]<=1:
					# {"feature": "Direction_same", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[8]<=0:
						return 'False'
					elif obj[8]>0:
						# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]<=6:
							return 'True'
						elif obj[4]>6:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		elif obj[6]<=1.0:
			# {"feature": "Distance", "instances": 22, "metric_value": 0.9024, "depth": 3}
			if obj[9]>1:
				# {"feature": "Coupon", "instances": 13, "metric_value": 0.6194, "depth": 4}
				if obj[2]>1:
					return 'False'
				elif obj[2]<=1:
					# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[5]>0.0:
						# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[7]>0.0:
							return 'True'
						elif obj[7]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[5]<=0.0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[9]<=1:
				# {"feature": "Occupation", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[4]<=13:
					# {"feature": "Direction_same", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[8]>0:
						# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[1]<=0:
							return 'True'
						elif obj[1]>0:
							return 'False'
						else: return 'False'
					elif obj[8]<=0:
						return 'True'
					else: return 'True'
				elif obj[4]>13:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[3]>3:
		# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[0]>1:
			# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[4]>1:
				return 'True'
			elif obj[4]<=1:
				return 'False'
			else: return 'False'
		elif obj[0]<=1:
			return 'True'
		else: return 'True'
	else: return 'True'
