def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[9]<=14:
		# {"feature": "Passanger", "instances": 28, "metric_value": 0.9852, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Distance", "instances": 21, "metric_value": 0.9852, "depth": 3}
			if obj[15]<=1:
				# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.684, "depth": 4}
				if obj[13]<=1.0:
					return 'False'
				elif obj[13]>1.0:
					return 'True'
				else: return 'True'
			elif obj[15]>1:
				# {"feature": "Coupon", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[3]>2:
					return 'True'
				elif obj[3]<=2:
					# {"feature": "Income", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[10]>2:
						# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[1]<=1:
							return 'True'
						elif obj[1]>1:
							return 'False'
						else: return 'False'
					elif obj[10]<=2:
						return 'False'
					else: return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[0]>1:
			return 'True'
		else: return 'True'
	elif obj[9]>14:
		return 'False'
	else: return 'False'
