def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[0]>0:
		# {"feature": "Coupon_validity", "instances": 31, "metric_value": 0.9812, "depth": 2}
		if obj[4]<=0:
			# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.8524, "depth": 3}
			if obj[13]<=1.0:
				# {"feature": "Time", "instances": 10, "metric_value": 1.0, "depth": 4}
				if obj[2]>0:
					# {"feature": "Coupon", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[3]<=2:
						return 'False'
					elif obj[3]>2:
						# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[8]<=0:
							return 'True'
						elif obj[8]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[2]<=0:
					return 'True'
				else: return 'True'
			elif obj[13]>1.0:
				return 'True'
			else: return 'True'
		elif obj[4]>0:
			# {"feature": "Coupon", "instances": 13, "metric_value": 0.9612, "depth": 3}
			if obj[3]<=3:
				# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[13]<=2.0:
					# {"feature": "Income", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[10]>0:
						return 'True'
					elif obj[10]<=0:
						return 'False'
					else: return 'False'
				elif obj[13]>2.0:
					return 'False'
				else: return 'False'
			elif obj[3]>3:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]<=0:
		return 'False'
	else: return 'False'
