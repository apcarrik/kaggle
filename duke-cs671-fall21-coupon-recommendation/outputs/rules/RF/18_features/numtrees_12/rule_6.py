def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9555, "depth": 1}
	if obj[3]>0:
		# {"feature": "Coffeehouse", "instances": 76, "metric_value": 0.8997, "depth": 2}
		if obj[13]<=3.0:
			# {"feature": "Education", "instances": 71, "metric_value": 0.8577, "depth": 3}
			if obj[9]>1:
				# {"feature": "Occupation", "instances": 37, "metric_value": 0.9569, "depth": 4}
				if obj[10]<=9:
					# {"feature": "Time", "instances": 26, "metric_value": 0.8404, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Coupon_validity", "instances": 20, "metric_value": 0.9341, "depth": 6}
						if obj[4]<=0:
							# {"feature": "Restaurantlessthan20", "instances": 12, "metric_value": 0.65, "depth": 7}
							if obj[14]>1.0:
								# {"feature": "Maritalstatus", "instances": 11, "metric_value": 0.4395, "depth": 8}
								if obj[7]<=1:
									return 'True'
								elif obj[7]>1:
									# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[0]<=1:
										return 'False'
									elif obj[0]>1:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[14]<=1.0:
								return 'False'
							else: return 'False'
						elif obj[4]>0:
							# {"feature": "Age", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[6]<=4:
								# {"feature": "Children", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[8]<=0:
									return 'False'
								elif obj[8]>0:
									# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[5]>0:
										return 'True'
									elif obj[5]<=0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[6]>4:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[2]>3:
						return 'True'
					else: return 'True'
				elif obj[10]>9:
					# {"feature": "Direction_same", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[16]<=0:
						# {"feature": "Age", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[6]>0:
							return 'False'
						elif obj[6]<=0:
							# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]>1:
								return 'False'
							elif obj[0]<=1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[16]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[9]<=1:
				# {"feature": "Weather", "instances": 34, "metric_value": 0.6723, "depth": 4}
				if obj[1]<=0:
					# {"feature": "Passanger", "instances": 23, "metric_value": 0.8281, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Bar", "instances": 12, "metric_value": 0.9799, "depth": 6}
						if obj[12]<=0.0:
							# {"feature": "Time", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[2]>0:
								return 'True'
							elif obj[2]<=0:
								return 'False'
							else: return 'False'
						elif obj[12]>0.0:
							# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[2]>0:
								return 'False'
							elif obj[2]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[0]>1:
						# {"feature": "Time", "instances": 11, "metric_value": 0.4395, "depth": 6}
						if obj[2]<=3:
							return 'True'
						elif obj[2]>3:
							# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[4]<=0:
								return 'True'
							elif obj[4]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				elif obj[1]>0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[13]>3.0:
			# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[10]<=6:
				return 'False'
			elif obj[10]>6:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[3]<=0:
		# {"feature": "Passanger", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[0]>0:
			return 'False'
		elif obj[0]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
