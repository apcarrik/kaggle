def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Income", "instances": 51, "metric_value": 0.9526, "depth": 1}
	if obj[13]>1:
		# {"feature": "Bar", "instances": 43, "metric_value": 0.8841, "depth": 2}
		if obj[14]>-1.0:
			# {"feature": "Coupon", "instances": 41, "metric_value": 0.839, "depth": 3}
			if obj[5]<=2:
				# {"feature": "Gender", "instances": 23, "metric_value": 0.5586, "depth": 4}
				if obj[7]>0:
					return 'True'
				elif obj[7]<=0:
					# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.8813, "depth": 5}
					if obj[17]>-1.0:
						# {"feature": "Weather", "instances": 9, "metric_value": 0.7642, "depth": 6}
						if obj[2]<=0:
							return 'True'
						elif obj[2]>0:
							# {"feature": "Age", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[8]>2:
								# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[12]>7:
									return 'True'
								elif obj[12]<=7:
									return 'False'
								else: return 'False'
							elif obj[8]<=2:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[17]<=-1.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[5]>2:
				# {"feature": "Passanger", "instances": 18, "metric_value": 0.9911, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Restaurantlessthan20", "instances": 13, "metric_value": 0.9612, "depth": 5}
					if obj[16]<=2.0:
						# {"feature": "Coupon_validity", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[6]>0:
							# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[8]<=4:
								return 'False'
							elif obj[8]>4:
								return 'True'
							else: return 'True'
						elif obj[6]<=0:
							return 'True'
						else: return 'True'
					elif obj[16]>2.0:
						return 'False'
					else: return 'False'
				elif obj[1]>2:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[14]<=-1.0:
			return 'False'
		else: return 'False'
	elif obj[13]<=1:
		# {"feature": "Driving_to", "instances": 8, "metric_value": 0.8113, "depth": 2}
		if obj[0]>0:
			return 'False'
		elif obj[0]<=0:
			# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[5]<=3:
				return 'True'
			elif obj[5]>3:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
