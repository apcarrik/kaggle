def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Distance", "instances": 85, "metric_value": 0.9991, "depth": 1}
	if obj[9]<=2:
		# {"feature": "Coupon", "instances": 76, "metric_value": 0.9875, "depth": 2}
		if obj[2]>0:
			# {"feature": "Occupation", "instances": 62, "metric_value": 0.9514, "depth": 3}
			if obj[4]<=19:
				# {"feature": "Bar", "instances": 58, "metric_value": 0.9689, "depth": 4}
				if obj[5]<=1.0:
					# {"feature": "Time", "instances": 41, "metric_value": 0.9012, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Education", "instances": 31, "metric_value": 0.9629, "depth": 6}
						if obj[3]>0:
							# {"feature": "Coffeehouse", "instances": 25, "metric_value": 0.9896, "depth": 7}
							if obj[6]<=3.0:
								# {"feature": "Restaurant20to50", "instances": 24, "metric_value": 0.995, "depth": 8}
								if obj[7]<=2.0:
									# {"feature": "Passanger", "instances": 23, "metric_value": 0.9986, "depth": 9}
									if obj[0]<=2:
										# {"feature": "Direction_same", "instances": 18, "metric_value": 1.0, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									elif obj[0]>2:
										# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]>2.0:
									return 'True'
								else: return 'True'
							elif obj[6]>3.0:
								return 'True'
							else: return 'True'
						elif obj[3]<=0:
							# {"feature": "Direction_same", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[8]<=0:
								return 'True'
							elif obj[8]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[1]>3:
						# {"feature": "Education", "instances": 10, "metric_value": 0.469, "depth": 6}
						if obj[3]>0:
							return 'True'
						elif obj[3]<=0:
							# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]<=1.0:
									return 'True'
								elif obj[6]>1.0:
									return 'False'
								else: return 'False'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[5]>1.0:
					# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.9774, "depth": 5}
					if obj[6]<=1.0:
						# {"feature": "Time", "instances": 11, "metric_value": 0.684, "depth": 6}
						if obj[1]>0:
							return 'False'
						elif obj[1]<=0:
							# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[7]>0.0:
									return 'False'
								elif obj[7]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[6]>1.0:
						# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[3]<=2:
							return 'True'
						elif obj[3]>2:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[4]>19:
				return 'True'
			else: return 'True'
		elif obj[2]<=0:
			# {"feature": "Bar", "instances": 14, "metric_value": 0.8631, "depth": 3}
			if obj[5]<=1.0:
				# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[7]<=2.0:
					return 'False'
				elif obj[7]>2.0:
					return 'True'
				else: return 'True'
			elif obj[5]>1.0:
				# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[0]>0:
					return 'True'
				elif obj[0]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[9]>2:
		# {"feature": "Coupon", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[2]<=2:
			return 'False'
		elif obj[2]>2:
			# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[5]<=0.0:
				return 'False'
			elif obj[5]>0.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
