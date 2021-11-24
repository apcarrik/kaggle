def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[7]>2:
		# {"feature": "Bar", "instances": 17, "metric_value": 0.9774, "depth": 2}
		if obj[9]<=2.0:
			# {"feature": "Age", "instances": 14, "metric_value": 0.8631, "depth": 3}
			if obj[4]>0:
				# {"feature": "Income", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[8]>0:
					# {"feature": "Passanger", "instances": 8, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Coupon", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[2]<=0:
							# {"feature": "Children", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[5]<=0:
								# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[11]<=1.0:
									return 'True'
								elif obj[11]>1.0:
									return 'False'
								else: return 'False'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[2]>0:
							return 'True'
						else: return 'True'
					elif obj[0]>1:
						return 'False'
					else: return 'False'
				elif obj[8]<=0:
					return 'False'
				else: return 'False'
			elif obj[4]<=0:
				return 'False'
			else: return 'False'
		elif obj[9]>2.0:
			return 'True'
		else: return 'True'
	elif obj[7]<=2:
		return 'True'
	else: return 'True'
