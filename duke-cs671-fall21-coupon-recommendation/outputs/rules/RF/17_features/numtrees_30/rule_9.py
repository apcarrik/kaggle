def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.9367, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Coffeehouse", "instances": 25, "metric_value": 0.9988, "depth": 2}
		if obj[13]>0.0:
			# {"feature": "Occupation", "instances": 21, "metric_value": 0.9587, "depth": 3}
			if obj[10]>2:
				# {"feature": "Direction_same", "instances": 17, "metric_value": 0.9975, "depth": 4}
				if obj[15]<=0:
					# {"feature": "Bar", "instances": 13, "metric_value": 0.9612, "depth": 5}
					if obj[12]<=0.0:
						# {"feature": "Income", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[11]>1:
							# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[3]>0:
								return 'True'
							elif obj[3]<=0:
								return 'False'
							else: return 'False'
						elif obj[11]<=1:
							return 'False'
						else: return 'False'
					elif obj[12]>0.0:
						return 'False'
					else: return 'False'
				elif obj[15]>0:
					return 'True'
				else: return 'True'
			elif obj[10]<=2:
				return 'True'
			else: return 'True'
		elif obj[13]<=0.0:
			return 'False'
		else: return 'False'
	elif obj[0]>1:
		return 'True'
	else: return 'True'
