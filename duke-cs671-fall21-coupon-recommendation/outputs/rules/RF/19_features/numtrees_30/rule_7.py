def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[0]>0:
		# {"feature": "Coupon", "instances": 30, "metric_value": 0.9481, "depth": 2}
		if obj[4]>0:
			# {"feature": "Education", "instances": 25, "metric_value": 0.9896, "depth": 3}
			if obj[10]>1:
				# {"feature": "Occupation", "instances": 13, "metric_value": 0.7793, "depth": 4}
				if obj[11]<=7:
					# {"feature": "Income", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[12]>1:
						# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[3]>0:
							return 'False'
						elif obj[3]<=0:
							return 'True'
						else: return 'True'
					elif obj[12]<=1:
						return 'True'
					else: return 'True'
				elif obj[11]>7:
					return 'False'
				else: return 'False'
			elif obj[10]<=1:
				# {"feature": "Bar", "instances": 12, "metric_value": 0.9183, "depth": 4}
				if obj[13]<=1.0:
					# {"feature": "Income", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[12]>3:
						# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[2]>55:
							# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[2]<=55:
							return 'True'
						else: return 'True'
					elif obj[12]<=3:
						return 'False'
					else: return 'False'
				elif obj[13]>1.0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[4]<=0:
			return 'False'
		else: return 'False'
	elif obj[0]<=0:
		return 'True'
	else: return 'True'
