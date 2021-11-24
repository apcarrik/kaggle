def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Maritalstatus", "instances": 85, "metric_value": 0.9637, "depth": 1}
	if obj[8]<=2:
		# {"feature": "Passanger", "instances": 81, "metric_value": 0.941, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Age", "instances": 52, "metric_value": 0.9957, "depth": 3}
			if obj[7]>1:
				# {"feature": "Time", "instances": 28, "metric_value": 0.9403, "depth": 4}
				if obj[3]>0:
					# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.9984, "depth": 5}
					if obj[16]>0.0:
						# {"feature": "Bar", "instances": 17, "metric_value": 0.9774, "depth": 6}
						if obj[13]<=1.0:
							# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.9957, "depth": 7}
							if obj[14]<=2.0:
								# {"feature": "Gender", "instances": 10, "metric_value": 0.8813, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[4]>0:
										return 'True'
									elif obj[4]<=0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[14]>2.0:
								return 'True'
							else: return 'True'
						elif obj[13]>1.0:
							return 'True'
						else: return 'True'
					elif obj[16]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[3]<=0:
					return 'False'
				else: return 'False'
			elif obj[7]<=1:
				# {"feature": "Direction_same", "instances": 24, "metric_value": 0.8113, "depth": 4}
				if obj[17]<=0:
					# {"feature": "Time", "instances": 17, "metric_value": 0.9367, "depth": 5}
					if obj[3]<=3:
						# {"feature": "Weather", "instances": 13, "metric_value": 0.9957, "depth": 6}
						if obj[1]<=0:
							# {"feature": "Education", "instances": 10, "metric_value": 0.971, "depth": 7}
							if obj[10]>0:
								# {"feature": "Children", "instances": 8, "metric_value": 0.8113, "depth": 8}
								if obj[9]<=0:
									return 'False'
								elif obj[9]>0:
									# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[11]<=5:
										return 'True'
									elif obj[11]>5:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[10]<=0:
								return 'True'
							else: return 'True'
						elif obj[1]>0:
							return 'True'
						else: return 'True'
					elif obj[3]>3:
						return 'True'
					else: return 'True'
				elif obj[17]>0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[0]>1:
			# {"feature": "Occupation", "instances": 29, "metric_value": 0.6632, "depth": 3}
			if obj[11]<=9:
				return 'True'
			elif obj[11]>9:
				# {"feature": "Income", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[12]<=7:
					# {"feature": "Time", "instances": 11, "metric_value": 0.8454, "depth": 5}
					if obj[3]>0:
						# {"feature": "Distance", "instances": 10, "metric_value": 0.7219, "depth": 6}
						if obj[18]>1:
							# {"feature": "Coupon_validity", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[4]>1:
									return 'False'
								elif obj[4]<=1:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[18]<=1:
							return 'True'
						else: return 'True'
					elif obj[3]<=0:
						return 'False'
					else: return 'False'
				elif obj[12]>7:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[8]>2:
		return 'False'
	else: return 'False'
