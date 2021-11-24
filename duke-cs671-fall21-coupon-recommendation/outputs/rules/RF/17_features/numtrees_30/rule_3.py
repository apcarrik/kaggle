def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Coffeehouse", "instances": 22, "metric_value": 0.9457, "depth": 2}
		if obj[13]>0.0:
			# {"feature": "Weather", "instances": 17, "metric_value": 0.9975, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.971, "depth": 4}
				if obj[14]<=1.0:
					# {"feature": "Coupon_validity", "instances": 11, "metric_value": 0.994, "depth": 5}
					if obj[4]<=0:
						# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[3]>0:
							return 'False'
						elif obj[3]<=0:
							# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=1:
								return 'True'
							elif obj[6]>1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[4]>0:
						# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[9]<=2:
							return 'True'
						elif obj[9]>2:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[14]>1.0:
					return 'False'
				else: return 'False'
			elif obj[1]>1:
				return 'True'
			else: return 'True'
		elif obj[13]<=0.0:
			return 'False'
		else: return 'False'
	elif obj[0]>2:
		# {"feature": "Coupon", "instances": 12, "metric_value": 0.8113, "depth": 2}
		if obj[3]>1:
			# {"feature": "Maritalstatus", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[7]<=2:
				return 'True'
			elif obj[7]>2:
				return 'False'
			else: return 'False'
		elif obj[3]<=1:
			return 'False'
		else: return 'False'
	else: return 'True'
