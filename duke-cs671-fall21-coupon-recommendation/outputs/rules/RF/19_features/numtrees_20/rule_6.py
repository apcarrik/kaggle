def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Education", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[10]>0:
		# {"feature": "Coupon_validity", "instances": 33, "metric_value": 0.9457, "depth": 2}
		if obj[5]<=0:
			# {"feature": "Distance", "instances": 23, "metric_value": 0.9986, "depth": 3}
			if obj[18]>1:
				# {"feature": "Age", "instances": 14, "metric_value": 0.8631, "depth": 4}
				if obj[7]<=2:
					# {"feature": "Gender", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[6]>0:
						# {"feature": "Income", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[12]>2:
							return 'False'
						elif obj[12]<=2:
							# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]<=1:
								return 'False'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[6]<=0:
						return 'True'
					else: return 'True'
				elif obj[7]>2:
					return 'False'
				else: return 'False'
			elif obj[18]<=1:
				# {"feature": "Coupon", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[4]<=3:
					return 'True'
				elif obj[4]>3:
					# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[0]>0:
						return 'False'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[5]>0:
			# {"feature": "Maritalstatus", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[8]<=1:
				return 'False'
			elif obj[8]>1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[10]<=0:
		# {"feature": "Age", "instances": 18, "metric_value": 0.7642, "depth": 2}
		if obj[7]>2:
			return 'True'
		elif obj[7]<=2:
			# {"feature": "Maritalstatus", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[8]>0:
				# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[3]<=1:
					return 'True'
				elif obj[3]>1:
					return 'False'
				else: return 'False'
			elif obj[8]<=0:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'True'
