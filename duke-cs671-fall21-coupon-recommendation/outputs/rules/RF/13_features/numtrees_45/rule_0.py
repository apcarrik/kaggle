def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[9]<=2.0:
		# {"feature": "Occupation", "instances": 18, "metric_value": 0.9641, "depth": 2}
		if obj[7]<=10:
			# {"feature": "Direction_same", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[11]<=0:
				# {"feature": "Coupon", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Age", "instances": 8, "metric_value": 1.0, "depth": 5}
					if obj[4]<=4:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[0]>0:
							return 'False'
						elif obj[0]<=0:
							# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1]<=0:
								return 'False'
							elif obj[1]>0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[4]>4:
						return 'True'
					else: return 'True'
				elif obj[2]>3:
					return 'False'
				else: return 'False'
			elif obj[11]>0:
				return 'True'
			else: return 'True'
		elif obj[7]>10:
			return 'True'
		else: return 'True'
	elif obj[9]>2.0:
		return 'False'
	else: return 'False'
