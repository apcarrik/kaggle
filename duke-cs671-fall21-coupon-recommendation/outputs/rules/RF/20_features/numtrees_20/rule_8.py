def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Coffeehouse", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[15]>1.0:
		# {"feature": "Restaurantlessthan20", "instances": 34, "metric_value": 0.9082, "depth": 2}
		if obj[16]<=3.0:
			# {"feature": "Passanger", "instances": 26, "metric_value": 0.7063, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Direction_same", "instances": 17, "metric_value": 0.874, "depth": 4}
				if obj[18]<=0:
					# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.994, "depth": 5}
					if obj[17]<=1.0:
						# {"feature": "Bar", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[14]>2.0:
							return 'True'
						elif obj[14]<=2.0:
							# {"feature": "Coupon_validity", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[6]<=0:
								return 'False'
							elif obj[6]>0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[17]>1.0:
						return 'False'
					else: return 'False'
				elif obj[18]>0:
					return 'True'
				else: return 'True'
			elif obj[1]>1:
				return 'True'
			else: return 'True'
		elif obj[16]>3.0:
			# {"feature": "Education", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[11]>1:
				return 'False'
			elif obj[11]<=1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[15]<=1.0:
		# {"feature": "Occupation", "instances": 17, "metric_value": 0.874, "depth": 2}
		if obj[12]>7:
			# {"feature": "Gender", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[7]<=0:
				# {"feature": "Coupon", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[5]>1:
					# {"feature": "Income", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[13]>4:
						# {"feature": "Driving_to", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[0]>0:
							# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[19]<=1:
								return 'True'
							elif obj[19]>1:
								return 'False'
							else: return 'False'
						elif obj[0]<=0:
							return 'False'
						else: return 'False'
					elif obj[13]<=4:
						return 'False'
					else: return 'False'
				elif obj[5]<=1:
					return 'True'
				else: return 'True'
			elif obj[7]>0:
				return 'True'
			else: return 'True'
		elif obj[12]<=7:
			return 'False'
		else: return 'False'
	else: return 'False'
