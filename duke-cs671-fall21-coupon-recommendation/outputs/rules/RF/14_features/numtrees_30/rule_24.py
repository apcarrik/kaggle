def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Income", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[8]>1:
		# {"feature": "Occupation", "instances": 27, "metric_value": 0.9751, "depth": 2}
		if obj[7]>1:
			# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 1.0, "depth": 3}
			if obj[11]<=1.0:
				# {"feature": "Passanger", "instances": 15, "metric_value": 0.9183, "depth": 4}
				if obj[0]>0:
					# {"feature": "Bar", "instances": 11, "metric_value": 0.684, "depth": 5}
					if obj[9]<=2.0:
						# {"feature": "Children", "instances": 10, "metric_value": 0.469, "depth": 6}
						if obj[5]<=0:
							return 'False'
						elif obj[5]>0:
							# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1]>0:
								return 'False'
							elif obj[1]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[9]>2.0:
						return 'True'
					else: return 'True'
				elif obj[0]<=0:
					# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[2]<=3:
						return 'True'
					elif obj[2]>3:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[11]>1.0:
				# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[2]>1:
					return 'True'
				elif obj[2]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[7]<=1:
			return 'True'
		else: return 'True'
	elif obj[8]<=1:
		return 'False'
	else: return 'False'
