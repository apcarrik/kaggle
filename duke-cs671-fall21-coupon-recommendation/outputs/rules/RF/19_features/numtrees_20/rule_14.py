def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[4]>0:
		# {"feature": "Occupation", "instances": 42, "metric_value": 0.9183, "depth": 2}
		if obj[11]>4:
			# {"feature": "Restaurant20to50", "instances": 25, "metric_value": 0.7219, "depth": 3}
			if obj[16]<=1.0:
				# {"feature": "Age", "instances": 17, "metric_value": 0.874, "depth": 4}
				if obj[7]>0:
					# {"feature": "Gender", "instances": 15, "metric_value": 0.7219, "depth": 5}
					if obj[6]<=0:
						# {"feature": "Coupon_validity", "instances": 9, "metric_value": 0.9183, "depth": 6}
						if obj[5]>0:
							# {"feature": "Income", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[12]>3:
								# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[14]<=3.0:
									return 'True'
								elif obj[14]>3.0:
									return 'False'
								else: return 'False'
							elif obj[12]<=3:
								return 'False'
							else: return 'False'
						elif obj[5]<=0:
							return 'True'
						else: return 'True'
					elif obj[6]>0:
						return 'True'
					else: return 'True'
				elif obj[7]<=0:
					return 'False'
				else: return 'False'
			elif obj[16]>1.0:
				return 'True'
			else: return 'True'
		elif obj[11]<=4:
			# {"feature": "Age", "instances": 17, "metric_value": 0.9975, "depth": 3}
			if obj[7]<=4:
				# {"feature": "Time", "instances": 14, "metric_value": 0.9403, "depth": 4}
				if obj[3]>0:
					# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.994, "depth": 5}
					if obj[14]>1.0:
						# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[10]<=2:
							return 'False'
						elif obj[10]>2:
							return 'True'
						else: return 'True'
					elif obj[14]<=1.0:
						# {"feature": "Maritalstatus", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[8]<=1:
							return 'True'
						elif obj[8]>1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[3]<=0:
					return 'False'
				else: return 'False'
			elif obj[7]>4:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[4]<=0:
		# {"feature": "Coupon_validity", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[5]<=0:
			return 'False'
		elif obj[5]>0:
			# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0]>0:
				return 'True'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
