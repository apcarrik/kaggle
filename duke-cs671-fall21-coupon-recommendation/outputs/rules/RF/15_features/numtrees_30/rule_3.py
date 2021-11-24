def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.9367, "depth": 1}
	if obj[7]>1:
		# {"feature": "Distance", "instances": 23, "metric_value": 0.9986, "depth": 2}
		if obj[14]<=2:
			# {"feature": "Income", "instances": 18, "metric_value": 0.9183, "depth": 3}
			if obj[9]>0:
				# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.7219, "depth": 4}
				if obj[12]>0.0:
					# {"feature": "Passanger", "instances": 13, "metric_value": 0.3912, "depth": 5}
					if obj[0]>0:
						return 'False'
					elif obj[0]<=0:
						# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1]>0:
							return 'False'
						elif obj[1]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[12]<=0.0:
					return 'True'
				else: return 'True'
			elif obj[9]<=0:
				return 'True'
			else: return 'True'
		elif obj[14]>2:
			return 'True'
		else: return 'True'
	elif obj[7]<=1:
		return 'True'
	else: return 'True'
