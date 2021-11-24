def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Bar", "instances": 51, "metric_value": 0.9183, "depth": 1}
	if obj[13]<=2.0:
		# {"feature": "Coupon", "instances": 44, "metric_value": 0.9624, "depth": 2}
		if obj[4]>1:
			# {"feature": "Distance", "instances": 35, "metric_value": 0.8631, "depth": 3}
			if obj[18]>1:
				# {"feature": "Age", "instances": 18, "metric_value": 0.9911, "depth": 4}
				if obj[7]>0:
					# {"feature": "Passanger", "instances": 15, "metric_value": 0.9183, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[14]<=2.0:
							# {"feature": "Income", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[12]>0:
								return 'False'
							elif obj[12]<=0:
								return 'True'
							else: return 'True'
						elif obj[14]>2.0:
							return 'True'
						else: return 'True'
					elif obj[0]>2:
						return 'True'
					else: return 'True'
				elif obj[7]<=0:
					return 'False'
				else: return 'False'
			elif obj[18]<=1:
				# {"feature": "Age", "instances": 17, "metric_value": 0.5226, "depth": 4}
				if obj[7]<=5:
					return 'True'
				elif obj[7]>5:
					# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[10]<=0:
						return 'True'
					elif obj[10]>0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[4]<=1:
			# {"feature": "Income", "instances": 9, "metric_value": 0.7642, "depth": 3}
			if obj[12]>0:
				return 'False'
			elif obj[12]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[13]>2.0:
		return 'True'
	else: return 'True'
