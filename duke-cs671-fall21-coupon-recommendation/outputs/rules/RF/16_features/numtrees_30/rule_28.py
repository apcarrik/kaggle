def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Income", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[10]>0:
		# {"feature": "Coupon", "instances": 26, "metric_value": 0.9829, "depth": 2}
		if obj[3]>1:
			# {"feature": "Coupon_validity", "instances": 19, "metric_value": 0.9819, "depth": 3}
			if obj[4]>0:
				# {"feature": "Age", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[6]>0:
					# {"feature": "Bar", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[11]>0.0:
						return 'False'
					elif obj[11]<=0.0:
						# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]<=3:
							return 'True'
						elif obj[2]>3:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[6]<=0:
					return 'True'
				else: return 'True'
			elif obj[4]<=0:
				# {"feature": "Age", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[6]<=4:
					# {"feature": "Time", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[2]<=2:
						return 'True'
					elif obj[2]>2:
						# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[5]<=0:
							return 'True'
						elif obj[5]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[6]>4:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[3]<=1:
			return 'False'
		else: return 'False'
	elif obj[10]<=0:
		return 'True'
	else: return 'True'
