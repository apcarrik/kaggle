def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[7]<=2:
		# {"feature": "Time", "instances": 18, "metric_value": 0.9183, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Income", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[9]<=4:
				# {"feature": "Coupon_validity", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[3]>0:
					# {"feature": "Age", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[5]<=2:
						# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[12]>0.0:
							return 'False'
						elif obj[12]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[5]>2:
						return 'True'
					else: return 'True'
				elif obj[3]<=0:
					return 'True'
				else: return 'True'
			elif obj[9]>4:
				return 'False'
			else: return 'False'
		elif obj[1]>2:
			return 'True'
		else: return 'True'
	elif obj[7]>2:
		return 'False'
	else: return 'False'
