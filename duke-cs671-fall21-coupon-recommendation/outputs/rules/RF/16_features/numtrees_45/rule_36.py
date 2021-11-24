def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Income", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[10]<=6:
		# {"feature": "Coupon", "instances": 20, "metric_value": 1.0, "depth": 2}
		if obj[3]<=3:
			# {"feature": "Gender", "instances": 16, "metric_value": 0.9544, "depth": 3}
			if obj[5]>0:
				# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 1.0, "depth": 4}
				if obj[13]<=1.0:
					# {"feature": "Bar", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[11]>0.0:
						return 'False'
					elif obj[11]<=0.0:
						# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[1]<=0:
							return 'True'
						elif obj[1]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[13]>1.0:
					return 'True'
				else: return 'True'
			elif obj[5]<=0:
				return 'True'
			else: return 'True'
		elif obj[3]>3:
			return 'False'
		else: return 'False'
	elif obj[10]>6:
		return 'True'
	else: return 'True'
