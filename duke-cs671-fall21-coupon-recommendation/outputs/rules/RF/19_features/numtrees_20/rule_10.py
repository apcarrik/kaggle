def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[11]<=14:
		# {"feature": "Coupon", "instances": 45, "metric_value": 0.9911, "depth": 2}
		if obj[4]>0:
			# {"feature": "Coupon_validity", "instances": 37, "metric_value": 0.9953, "depth": 3}
			if obj[5]>0:
				# {"feature": "Time", "instances": 21, "metric_value": 0.9183, "depth": 4}
				if obj[3]<=3:
					# {"feature": "Income", "instances": 14, "metric_value": 0.5917, "depth": 5}
					if obj[12]>0:
						# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.3912, "depth": 6}
						if obj[14]>0.0:
							return 'False'
						elif obj[14]<=0.0:
							# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]>0:
								return 'False'
							elif obj[6]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[12]<=0:
						return 'True'
					else: return 'True'
				elif obj[3]>3:
					# {"feature": "Age", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[7]<=2:
						return 'True'
					elif obj[7]>2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[5]<=0:
				# {"feature": "Bar", "instances": 16, "metric_value": 0.6962, "depth": 4}
				if obj[13]>0.0:
					# {"feature": "Age", "instances": 13, "metric_value": 0.3912, "depth": 5}
					if obj[7]>0:
						return 'True'
					elif obj[7]<=0:
						return 'False'
					else: return 'False'
				elif obj[13]<=0.0:
					# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[7]>1:
						return 'False'
					elif obj[7]<=1:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[4]<=0:
			return 'False'
		else: return 'False'
	elif obj[11]>14:
		return 'True'
	else: return 'True'
