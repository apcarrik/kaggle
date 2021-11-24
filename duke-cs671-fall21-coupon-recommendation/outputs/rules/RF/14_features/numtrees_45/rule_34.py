def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[7]<=12:
		# {"feature": "Time", "instances": 18, "metric_value": 0.9641, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Income", "instances": 15, "metric_value": 0.8366, "depth": 3}
			if obj[8]>2:
				# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[10]<=2.0:
					# {"feature": "Coupon", "instances": 8, "metric_value": 1.0, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[11]>0.0:
							return 'True'
						elif obj[11]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[2]>2:
						return 'False'
					else: return 'False'
				elif obj[10]>2.0:
					return 'True'
				else: return 'True'
			elif obj[8]<=2:
				return 'True'
			else: return 'True'
		elif obj[1]>3:
			return 'False'
		else: return 'False'
	elif obj[7]>12:
		return 'False'
	else: return 'False'
