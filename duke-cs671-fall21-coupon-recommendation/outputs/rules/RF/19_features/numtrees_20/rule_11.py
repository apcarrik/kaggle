def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[11]<=19:
		# {"feature": "Education", "instances": 45, "metric_value": 0.9825, "depth": 2}
		if obj[10]<=2:
			# {"feature": "Age", "instances": 33, "metric_value": 0.885, "depth": 3}
			if obj[7]>3:
				# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.9819, "depth": 4}
				if obj[16]>0.0:
					# {"feature": "Coupon", "instances": 16, "metric_value": 1.0, "depth": 5}
					if obj[4]<=2:
						# {"feature": "Income", "instances": 9, "metric_value": 0.9183, "depth": 6}
						if obj[12]>3:
							# {"feature": "Restaurantlessthan20", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[15]<=2.0:
								return 'True'
							elif obj[15]>2.0:
								return 'False'
							else: return 'False'
						elif obj[12]<=3:
							return 'False'
						else: return 'False'
					elif obj[4]>2:
						# {"feature": "Bar", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[13]>0.0:
							return 'True'
						elif obj[13]<=0.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[16]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[7]<=3:
				# {"feature": "Passanger", "instances": 14, "metric_value": 0.5917, "depth": 4}
				if obj[0]<=1:
					return 'False'
				elif obj[0]>1:
					# {"feature": "Children", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[9]<=0:
						# {"feature": "Income", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[12]<=6:
							return 'True'
						elif obj[12]>6:
							return 'False'
						else: return 'False'
					elif obj[9]>0:
						return 'False'
					else: return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[10]>2:
			# {"feature": "Coupon", "instances": 12, "metric_value": 0.8113, "depth": 3}
			if obj[4]>1:
				# {"feature": "Restaurantlessthan20", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[15]<=3.0:
					return 'True'
				elif obj[15]>3.0:
					return 'False'
				else: return 'False'
			elif obj[4]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[11]>19:
		return 'True'
	else: return 'True'
