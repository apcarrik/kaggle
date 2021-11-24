def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Passanger", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[0]>0:
		# {"feature": "Education", "instances": 46, "metric_value": 0.9945, "depth": 2}
		if obj[3]<=2:
			# {"feature": "Coupon", "instances": 34, "metric_value": 0.9367, "depth": 3}
			if obj[2]>1:
				# {"feature": "Occupation", "instances": 29, "metric_value": 0.8498, "depth": 4}
				if obj[4]<=9:
					# {"feature": "Coffeehouse", "instances": 20, "metric_value": 0.6098, "depth": 5}
					if obj[6]>1.0:
						# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.8813, "depth": 6}
						if obj[7]>0.0:
							# {"feature": "Time", "instances": 9, "metric_value": 0.7642, "depth": 7}
							if obj[1]<=3:
								return 'True'
							elif obj[1]>3:
								# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[5]<=1.0:
									return 'False'
								elif obj[5]>1.0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[7]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[6]<=1.0:
						return 'True'
					else: return 'True'
				elif obj[4]>9:
					# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[6]<=3.0:
						# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[9]<=2:
							# {"feature": "Bar", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[5]>0.0:
								return 'False'
							elif obj[5]<=0.0:
								# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[1]<=0:
									# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[9]>2:
							return 'True'
						else: return 'True'
					elif obj[6]>3.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[2]<=1:
				# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]>5:
						# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]>0.0:
							return 'False'
						elif obj[5]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[4]<=5:
						return 'False'
					else: return 'False'
				elif obj[1]>1:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[3]>2:
			# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.8113, "depth": 3}
			if obj[7]<=2.0:
				# {"feature": "Occupation", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[4]>4:
					return 'False'
				elif obj[4]<=4:
					# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[6]>0.0:
						# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[2]<=2:
								# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[5]<=0.0:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[9]<=3:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[6]<=0.0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[7]>2.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]<=0:
		return 'True'
	else: return 'True'
