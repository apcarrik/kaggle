def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Income", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[11]<=6:
		# {"feature": "Occupation", "instances": 20, "metric_value": 0.9341, "depth": 2}
		if obj[10]<=19:
			# {"feature": "Coffeehouse", "instances": 18, "metric_value": 0.8524, "depth": 3}
			if obj[13]<=2.0:
				# {"feature": "Coupon_validity", "instances": 16, "metric_value": 0.6962, "depth": 4}
				if obj[4]>0:
					# {"feature": "Children", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[8]<=0:
						# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[3]>1:
							# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[9]<=2:
								return 'False'
							elif obj[9]>2:
								return 'True'
							else: return 'True'
						elif obj[3]<=1:
							return 'True'
						else: return 'True'
					elif obj[8]>0:
						return 'False'
					else: return 'False'
				elif obj[4]<=0:
					return 'False'
				else: return 'False'
			elif obj[13]>2.0:
				return 'True'
			else: return 'True'
		elif obj[10]>19:
			return 'True'
		else: return 'True'
	elif obj[11]>6:
		return 'True'
	else: return 'True'
