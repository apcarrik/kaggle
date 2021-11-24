def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[2]<=3:
		# {"feature": "Age", "instances": 17, "metric_value": 0.9367, "depth": 2}
		if obj[4]<=5:
			# {"feature": "Education", "instances": 15, "metric_value": 0.8366, "depth": 3}
			if obj[6]<=2:
				# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[10]>0.0:
					# {"feature": "Passanger", "instances": 8, "metric_value": 1.0, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[1]>0:
							return 'False'
						elif obj[1]<=0:
							# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[7]<=2:
								return 'True'
							elif obj[7]>2:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[0]>2:
						return 'True'
					else: return 'True'
				elif obj[10]<=0.0:
					return 'True'
				else: return 'True'
			elif obj[6]>2:
				return 'True'
			else: return 'True'
		elif obj[4]>5:
			return 'False'
		else: return 'False'
	elif obj[2]>3:
		# {"feature": "Age", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[4]<=4:
			return 'False'
		elif obj[4]>4:
			return 'True'
		else: return 'True'
	else: return 'False'
