def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[1]>0:
		# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.9975, "depth": 2}
		if obj[9]<=2.0:
			# {"feature": "Age", "instances": 13, "metric_value": 0.9612, "depth": 3}
			if obj[4]>1:
				# {"feature": "Occupation", "instances": 10, "metric_value": 1.0, "depth": 4}
				if obj[7]>1:
					# {"feature": "Coupon", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[0]>0:
							# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[3]<=0:
								# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[8]>0.0:
									return 'False'
								elif obj[8]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[3]>0:
								return 'False'
							else: return 'False'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					elif obj[2]>3:
						return 'False'
					else: return 'False'
				elif obj[7]<=1:
					return 'True'
				else: return 'True'
			elif obj[4]<=1:
				return 'True'
			else: return 'True'
		elif obj[9]>2.0:
			return 'False'
		else: return 'False'
	elif obj[1]<=0:
		return 'True'
	else: return 'True'
