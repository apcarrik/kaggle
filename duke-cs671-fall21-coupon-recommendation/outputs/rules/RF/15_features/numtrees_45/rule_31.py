def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.8281, "depth": 1}
	if obj[7]>0:
		# {"feature": "Occupation", "instances": 17, "metric_value": 0.9367, "depth": 2}
		if obj[8]<=11:
			# {"feature": "Coupon", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[2]>0:
				# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[11]>-1.0:
					# {"feature": "Bar", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[10]>0.0:
						# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[5]>0:
								return 'True'
							elif obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[0]>2:
							return 'False'
						else: return 'False'
					elif obj[10]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[11]<=-1.0:
					return 'False'
				else: return 'False'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		elif obj[8]>11:
			return 'True'
		else: return 'True'
	elif obj[7]<=0:
		return 'True'
	else: return 'True'
