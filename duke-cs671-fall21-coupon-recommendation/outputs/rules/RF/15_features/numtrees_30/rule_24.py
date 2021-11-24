def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Income", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[9]<=4:
		# {"feature": "Bar", "instances": 23, "metric_value": 0.9877, "depth": 2}
		if obj[10]>0.0:
			# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.971, "depth": 3}
			if obj[12]<=1.0:
				# {"feature": "Time", "instances": 13, "metric_value": 0.8905, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Distance", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[14]>1:
						# {"feature": "Coupon_validity", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[3]<=0:
							return 'True'
						elif obj[3]>0:
							# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]>1:
								return 'True'
							elif obj[0]<=1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[14]<=1:
						# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[5]<=3:
							return 'False'
						elif obj[5]>3:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[1]>2:
					return 'True'
				else: return 'True'
			elif obj[12]>1.0:
				return 'False'
			else: return 'False'
		elif obj[10]<=0.0:
			# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[12]>-1.0:
				return 'False'
			elif obj[12]<=-1.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[9]>4:
		# {"feature": "Age", "instances": 11, "metric_value": 0.4395, "depth": 2}
		if obj[5]>0:
			return 'True'
		elif obj[5]<=0:
			return 'False'
		else: return 'False'
	else: return 'True'
