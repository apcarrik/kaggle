def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Coupon", "instances": 41, "metric_value": 0.9996, "depth": 1}
	if obj[5]>1:
		# {"feature": "Direction_same", "instances": 31, "metric_value": 0.9383, "depth": 2}
		if obj[19]<=0:
			# {"feature": "Restaurant20to50", "instances": 25, "metric_value": 0.9896, "depth": 3}
			if obj[18]>0.0:
				# {"feature": "Income", "instances": 20, "metric_value": 0.9928, "depth": 4}
				if obj[13]>0:
					# {"feature": "Education", "instances": 16, "metric_value": 0.9887, "depth": 5}
					if obj[11]<=2:
						# {"feature": "Gender", "instances": 11, "metric_value": 0.9457, "depth": 6}
						if obj[7]>0:
							# {"feature": "Distance", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[20]<=2:
								return 'False'
							elif obj[20]>2:
								return 'True'
							else: return 'True'
						elif obj[7]<=0:
							# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[1]>0:
								return 'True'
							elif obj[1]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[11]>2:
						return 'True'
					else: return 'True'
				elif obj[13]<=0:
					return 'False'
				else: return 'False'
			elif obj[18]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[19]>0:
			return 'True'
		else: return 'True'
	elif obj[5]<=1:
		# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[18]<=2.0:
			return 'False'
		elif obj[18]>2.0:
			return 'True'
		else: return 'True'
	else: return 'False'
